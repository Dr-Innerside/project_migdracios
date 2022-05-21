const BE_BASE_URL = "http://127.0.01:5000/"
const FE_BASE_URL = "http://127.0.01:5500/"

// 비동기 함수 선언
async function handleSignUp() {

    const signupData = {
        email: document.getElementById('floatingInput').value,
        password: document.getElementById('floatingPassword').value
    }


    // 언제 들어올지 모르니까 일단 대기
    const response = await fetch('${BE_BASE_URL}/signup', {
        method: 'POST',
        body: JSON.stringify(signupData)
    })
    console.log('response check in SIGNUP')
    console.log(response)

}