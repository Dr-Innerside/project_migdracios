// 비동기 함수 선언
async function handleSignin() {

    const signupData = {
        email: document.getElementById('floatingInput').value,
        password: document.getElementById('floatingPassword').value
    }

    console.log(email, password)

    const response = await fetch('http:127.0.0.1:5000/signup', {
        method: 'POST',
        body: signupData
    })


}