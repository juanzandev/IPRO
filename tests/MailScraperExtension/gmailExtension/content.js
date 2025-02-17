// Debug
console.log('Content script loaded');
// Wait for Gmail to load
window.addEventListener('load', function () {
    // Debug
    console.log('Page loaded, starting observer');

    const observer = new MutationObserver(() => {
        // Generic and reliable?? Hopefully
        const emailView = document.querySelector('div[role="dialog"], .nH.bkK');

        if (emailView) {
            console.log('Email view detect:', emailView);

            // Add a click event for opening an email
            emailView.addEventListener('click', function () {
                console.log('Email clicked!');
            

                // Delay to allow dynamic loading
                setTimeout(() => {
                    const subjectElement = emailView.querySelector('.nH'); // Potention: .zA.yO
                    const bodyElement = emailView.querySelector('.Bk');

                    const subject = subjectElement ? subjectElement.innerText : "No subject found";
                    const body = bodyElement ? bodyElement.innerText : "No body found";

                    // Debug
                    console.log('Email clicked!');
                    console.log('Subject:', subject);
                    console.log('Body:', body.substring(0, 100) + '...'); //display first 100 characters

                    // Send email data to the background script
                    chrome.runtime.sendMessage({
                        type: 'emailContent',
                        subject: subject,
                        body: body
                    });

                    // Mark email as processed to prevent multiple POSTs
                    emailView.dataset.processed = true;

                }, 500) //500 ms delay
            });

            // Reset the processed state when the email is closed
            emailView.addEventListener('transitionend', function() {
                if (emailView.computedStyleMap.display === "none") {
                    console.log('Email dialog closed, resetting processed state.');
                    delete emailView.dataset.processed; // Reset processed state when email is closed
                }
            })
        }
    });

    // Observe changes in Gmail's DOM
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
});