const BE_BASE_URL = "http://127.0.0.1:5000"
const FE_BASE_URL = "http://127.0.0.1:5500"

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
        window.location.replace('http://127.0.0.1:5500/frontend/login.html')
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
        console.log(localStorage.token)
        window.location.replace('http://127.0.01:5500/frontend/index.html')
    }

    else if(response.status == 202) {
        alert(response_json['msg'])
    }

    else if(response.status == 203) {
        alert(response_json['msg'])
    }
}

async function getUserName(){
    console.log('loading userName')

    const response = await fetch(`${BE_BASE_URL}/getname`, {
        headers: {
            'Authorization': localStorage.getItem("token")
        }
    })
    // console.log(response)
    response_json = await response.json()
    console.log(response_json)

    user_id = response_json['user_id'].split('@')[0]
    console.log('user_id : ', user_id)

    const element_username = document.getElementById("user_name")
    
    element_username.innerText = response_json.user_id

}


