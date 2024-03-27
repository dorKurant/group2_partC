const login = document.querySelector('#login-container')
const msg = document.querySelector('.msg')
const username=document.querySelector('#username_input')
const password=document.querySelector('#password_input')

const onSubmit =(e) =>{
    // e.preventDefault()
    console.log(username.value)
    if(username.value==='' || password.value==='')
    {
        msg.innerHTML='please enter all fields !'
        // setTimeout(()=>{
        //     msg.innerHTML=''
        //     msg.classList.remove('error',10000)
        // })
    }
    else
    {
        username.value=''
        password.value=''
        msg.innerHTML=''
        // window.location.href = "/SFS";

    }

}
login.addEventListener('submit',onSubmit)