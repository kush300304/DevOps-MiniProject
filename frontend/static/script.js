const form = document.getElementById('loginForm');
const toggleBtn = document.getElementById('toggleForm');
const messageDiv = document.getElementById('message');
let isLogin = true;

toggleBtn.addEventListener('click', () => {
    isLogin = !isLogin;
    form.querySelector('button').textContent = isLogin ? 'Login' : 'Signup';
    toggleBtn.textContent = isLogin ? 'Switch to Signup' : 'Switch to Login';
});

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    try {
        const response = await fetch(`/${isLogin ? 'login' : 'signup'}`, {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            messageDiv.textContent = data.message;
            messageDiv.style.color = data.status === "error" ? 'red' : 'green';
        } else {
            messageDiv.textContent = data.detail;
            messageDiv.style.color = 'red';
        }
    } catch (error) {
        messageDiv.textContent = 'An error occurred. Please try again.';
        messageDiv.style.color = 'red';
    }
});