// Lấy các phần tử form và nút
const loginForm = document.getElementById('loginForm');
const registerForm = document.getElementById('registerForm');
const closeBtn = document.getElementById('closeBtn');
const closeRegisterBtn = document.getElementById('closeRegisterBtn');

// Các phần tử của form đăng nhập
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const usernameError = document.getElementById('usernameError');
const passwordError = document.getElementById('passwordError');

// Các phần tử của form đăng ký
const userNameInput = document.getElementById('user_name');
const emailInput = document.getElementById('email');
const registerPasswordInput = document.getElementById('register_password');
const confirmPasswordInput = document.getElementById('confirm_password');
const userNameError = document.getElementById('userNameError');
const emailError = document.getElementById('emailError');
const registerPasswordError = document.getElementById('registerPasswordError');
const confirmPasswordError = document.getElementById('confirmPasswordError');

// Mở form đăng ký
document.querySelector('.btn').addEventListener('click', () => {
    document.getElementById('loginFrame').classList.add('hidden');
    document.getElementById('registerFrame').classList.remove('hidden');
});

// Mở form đăng nhập
document.querySelector('.btn-red-sn').addEventListener('click', () => {
    document.getElementById('registerFrame').classList.add('hidden');
    document.getElementById('loginFrame').classList.remove('hidden');
});

// Đóng form đăng nhập
closeBtn.addEventListener('click', () => {
    document.getElementById('loginFrame').classList.add('hidden');
});

// Đóng form đăng ký
closeRegisterBtn.addEventListener('click', () => {
    document.getElementById('registerFrame').classList.add('hidden');
});

// Kiểm tra đăng nhập
loginForm.addEventListener('submit', function (e) {
    e.preventDefault();

    // Reset lỗi cũ
    usernameError.style.display = 'none';
    passwordError.style.display = 'none';

    // Kiểm tra form đăng nhập
    const username = usernameInput.value.trim();
    const password = passwordInput.value.trim();

    if (!username) {
        usernameError.style.display = 'block';
    }
    if (!password) {
        passwordError.style.display = 'block';
    }

    if (username && password) {
        // Thực hiện đăng nhập tại đây
        console.log("Đăng nhập thành công");
    }
});

// Kiểm tra đăng ký
registerForm.addEventListener('submit', function (e) {
    e.preventDefault();

    // Reset lỗi cũ
    userNameError.style.display = 'none';
    emailError.style.display = 'none';
    registerPasswordError.style.display = 'none';
    confirmPasswordError.style.display = 'none';

    // Kiểm tra form đăng ký
    const userName = userNameInput.value.trim();
    const email = emailInput.value.trim();
    const registerPassword = registerPasswordInput.value.trim();
    const confirmPassword = confirmPasswordInput.value.trim();

    let valid = true;

    if (!userName) {
        userNameError.style.display = 'block';
        valid = false;
    }

    if (!email || !/\S+@\S+\.\S+/.test(email)) {
        emailError.style.display = 'block';
        valid = false;
    }

    if (!registerPassword) {
        registerPasswordError.style.display = 'block';
        valid = false;
    }

    if (registerPassword !== confirmPassword) {
        confirmPasswordError.style.display = 'block';
        valid = false;
    }

    if (valid) {
        // Thực hiện đăng ký tại đây
        console.log("Đăng ký thành công");
    }
});
