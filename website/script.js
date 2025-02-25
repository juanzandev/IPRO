 <script>
        function signIn() {
            const email = document.getElementById('signin-email').value;
            const password = document.getElementById('signin-password').value;

            // Simulate authentication check (replace with your actual logic)
            if (email === 'test@example.com' && password === 'password') {
                alert(`Signing in with Email: ${email}`); // Successful login
            } else {
                // Show the error message
                document.getElementById('signin-error').style.display = 'block';
                return;
            }

            // Hide the error message on successful or subsequent attempts
            document.getElementById('signin-error').style.display = 'none';
            // Add your sign-in logic here (e.g., sending data to a server)
        }

        function signUp() {
            const email = document.getElementById('signup-email').value;
            const password = document.getElementById('signup-password').value;
            const retypePassword = document.getElementById('signup-retype-password').value;

            if (password !== retypePassword) {
                alert("Passwords do not match!");
                return;
            }

            alert(`Signing up with Email: ${email}`);
            // Add your sign-up logic here (e.g., sending data to a server)
        }
    </script>
