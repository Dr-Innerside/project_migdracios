// 비동기 함수 선언
async function handleSignin() {

    const signupData = {
        email: document.getElementById('floatingInput').value,
        password: document.getElementById('floatingPassword').value
    }

    const response = await fetch('http://127.0.0.1:5000/signup', {
        method: 'POST',
        body: signupData
    })
    console.log(response)

}