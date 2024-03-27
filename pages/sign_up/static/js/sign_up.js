

const form = document.getElementById('form_')
const firstName = document.querySelector('#firstName')
const lastName = document.querySelector('#lastName')
const userName = document.querySelector('#userName')
const password = document.querySelector('#password')
const universityMail = document.querySelector('#universityMail')
const phoneNumber = document.querySelector('#phoneNumber')
const address = document.querySelector('#address')
const msg = document.querySelector('#msg')

const onSubmit = (e)=> {

    let formTakin = true;
    // session['formTakin'] = true;
    if (firstName.value === "" || lastName.value === "") {
        msg.innerText += 'First and last name are required!\n'
        formTakin = false;
        e.preventDefault()
        // session['formTakin'] = false;
    }
    if (userName.value === "") {
        msg.innerText += 'Please choose a user name!\n'
        formTakin = false;
        e.preventDefault()
        // session['formTakin'] = false;

    }
    if (password.value === ""|| password.value.length<8){
        msg.innerText += 'Please choose a valid password with at least 8 characters!\n'
        formTakin = false;
        e.preventDefault()
        // session['formTakin'] = false;

    }
    const companyEmailRegex = /@post.bgu\.ac.il$/;
      if (universityMail.value === ""||!companyEmailRegex.test(universityMail.value)){
        msg.innerText += 'Please enter your university mail!\n'
        formTakin = false;
        e.preventDefault()
    }
      const phoneNumberRegex = /^\d+$/;
      if (phoneNumber.value === ""||phoneNumber.value.length<10||phoneNumber.value.length>10
          ||!phoneNumberRegex.test(phoneNumber.value)){
        msg.innerText += 'Please a valid phone number with 10 digit numbers\n'
        formTakin = false;
        e.preventDefault()
    }

      if (address.value === "") {
          msg.innerText += 'Please enter your address!\n'
          formTakin = false;
          e.preventDefault()
      }
        if (formTakin == false)
            setTimeout(() => {
                msg.innerText = "";
        }, 4000);
}
form.addEventListener('submit', onSubmit);

