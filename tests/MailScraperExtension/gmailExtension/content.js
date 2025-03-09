console.log('Content script loaded');

// Hold the timeout to prevent multple triggers
let debounceTimeout = null;

// Observe changes in Gmail's email view
const observer = new MutationObserver(() => {
    const emailView = document.querySelector('div[role="dialog"], .nH.bkK'); // Detects opened email

    if (emailView) {
        console.log('Email view detected:', emailView);

        // Clear the existing timeout to prevent multiple triggers
        clearTimeout(debounceTimeout);

        // Set a timeout to ensure content is fully loaded and prevent rapid repeated calls
        debounceTimeout = setTimeout(() => {
            const subjectElement = emailView.querySelector('.hP'); // Subject selector
            const bodyElement = emailView.querySelector('.ii.gt'); // Body selector
            const senderNameElement = emailView.querySelector('.gD') // Sender name
            const senderEmailElement = senderNameElement ? senderNameElement.getAttribute('email') : null; // Sender email

            const subject = subjectElement ? subjectElement.innerText : "No subject found";
            const body = bodyElement ? bodyElement.innerText : "No body found";
            const senderName = senderNameElement ? senderNameElement.innerText : "No sender name found";
            const senderEmail = senderEmailElement ? senderEmailElement : "No sender email found";

            console.log('Sending email to server:', subject);

            // Send email data to the background script (stateless approach)
            chrome.runtime.sendMessage({
                type: 'emailContent',
                subject: subject,
                body: body,
                senderName: senderName,
                senderEmail: senderEmail
            });

        }, 500); // Delay ensures content is fully loaded
    }
});

// Observe Gmail's DOM for email view changes
observer.observe(document.body, {
    childList: true,
    subtree: true
});