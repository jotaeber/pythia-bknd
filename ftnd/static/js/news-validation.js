
// Nodos
const formAlta = document.querySelector('#form-alta');
const p = document.createElement('p');

const validationForm = (event) => {
    event.preventDefault();
    
    const name = document.querySelector('#nombre');

    let validation = true;
    
    if(name.value === ''){
        const divError = document.querySelector('#error-nombre');
        divError.textContent='Falta agregar datos en el campo';
        validation = false;
    
    if(validation){
        formAlta.submit();
    }
}

formAlta.addEventListener('submit',validationForm);
