
// Nodos
const formFaq = document.querySelector('#form-faq');
const p = document.createElement('p');

const validationForm = (event) => {
    event.preventDefault();
    
    const name = document.querySelector('#nombre');
    const email = document.querySelector('#email');
    const subject = document.querySelector('#motivo');
    const query = document.querySelector('#consulta')

    let validation = true;
    
    if(name.value === ''){
        const divError = document.querySelector('#error-nombre');
        divError.textContent='Por favor, ingrese un nombre';
        validation = false;
    }
    if(email.value === ''){
        const divError = document.querySelector('#error-email');
        divError.textContent='Por favor, ingrese un email';
        validation = false;
    }
    if(subject.value === ''){
        const divError = document.querySelector('#error-motivo');
        divError.textContent='Por favor, ingrese un motivo';
        validation = false;
    }
    if(query.value === ''){
        const divError = document.querySelector('#error-consulta');
        divError.textContent='Por favor, ingrese su consulta para poder ayudarle';
        validation = false;
    }
    
    if(validation){
        formFaq.submit();
    }
}

formFaq.addEventListener('submit',validationForm);
