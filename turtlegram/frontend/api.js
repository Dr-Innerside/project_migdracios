const BE_BASE_URL = "http://127.0.01:5000"
const FE_BASE_URL = "http://127.0.01:5500"

// 비동기 함수 선언
async function handleSignUp() {

    const signupData = {
        email: document.getElementById('floatingInput').value,
        password: document.getElementById('floatingPassword').value
    }
    console.log(signupData)

    // 언제 들어올지 모르니까 일단 대기
    const response = await fetch('http://127.0.0.1:5000/signup', {
        method: 'POST',
        body: JSON.stringify(signupData)
    })
    // console.log('response check in SIGNUP')
    // console.log(response['msg'])

    response_json = await response.json()
    console.log(response_json)
    
    if (response.status == 201) {
        alert(response_json['msg'])
        window.location.replace('http://127.0.01:5500/frontend/login.html')
    }

    else if(response.status == 202) {
        alert(response_json['msg'])
    }

    else if(response.status == 203) {
        alert(response_json['msg'])
    }
}

function goToSignUp(){
    window.location.replace('http://127.0.01:5500/signup.html')
}

async function handleSignIn(){
    const signupData = {
        email: document.getElementById('floatingInput').value,
        password: document.getElementById('floatingPassword').value
    }
    console.log(signupData)

    // 언제 들어올지 모르니까 일단 대기
    const response = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        body: JSON.stringify(signupData)
    })

    response_json = await response.json()
    console.log(response_json)
    
    if (response.status == 201) {
        alert(response_json['msg'])
        localStorage.setItem("token", response_json['token'])
    }

    else if(response.status == 202) {
        alert(response_json['msg'])
    }

    else if(response.status == 203) {
        alert(response_json['msg'])
    }
}