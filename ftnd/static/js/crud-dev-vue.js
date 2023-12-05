
const { createApp } = Vue;
createApp({
  data() {
    return {
        students : [],
        api_server:"http://127.0.0.1:8000",
        id_student:'',
        name:'',
        surname:'',
        birth_date:'',
        course:'',
        email:'',
        ssn:'',
    };
  },
  methods: {
    sendFormData(url, formData,method) {
        fetch(url, {
          method: method,
          body: formData,
        })
        .then((response) => response.json())
        .then((data) => {
            alert("Registro creado:");
            this.getStudents(`${this.api_server}/api/get_students`);
        })
        .catch((error) => {
            console.error("Error al enviar el formulario:", error);
        });
    },
    
    getStudents() {
      fetch(`${this.api_server}/api/get_students`)
        .then((response) => response.json())
        .then((data) => {
          this.students = data;
          this.cargando = false;
        })
        .catch((err) => {
          console.error(err);
          this.error = true;
        });
    },
    getStudents(id_student) {
        fetch(`${this.api_server}/api/get_students/${id_student}/`, {
            method: 'GET',
        })
        .then((response) => response.json())
        .then((data) => {
            this.id_student = data.id;
            this.name = data.name;
            this.surname = data.surname;
            this.birth_date = data.birth_date;
            this.course = data.course;
            this.email = data.email;
            this.ssn = data.ssn;
            console.log(data);
        })
        .catch((error) => {
            console.error("Error al enviar el formulario:", error);
        });
    },
   
    saveMovie() {
        const formData = new FormData();
        formData.append('name', this.name);
        formData.append('surname', this.surname);
        formData.append('birth_date', this.birth_date);
        formData.append('course', this.course);
        formData.append('email', this.email);
        formData.append('ssn', this.ssn);
        if(this.id_student){
            this.sendFormData(`${this.api_server}/api/modify_student/${this.id_student}/`, formData,'PUT');
        }else{
            this.sendFormData(`${this.api_server}/api/add_student/`, formData,'POST');
        }
    },
    deleteMovie(id_student) {
        console.log('teasd');
        fetch(`${this.api_server}/api/delete_student/${id_student}/`, {
            method: 'DELETE',
        })
        .then((response) => response.json())
        .then((data) => {
            alert("Registro Eliminado");
            this.getStudents(`${this.api_server}/api/get_students`);
        })
        .catch((error) => {
            console.error("Error al eliminar", error);
        });
    },
  },
  created() {
    this.getStudents();
  },
}).mount("#app");
