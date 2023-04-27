const socios = [
    { id: 12, name: 'deivicho'},
    { id: 2, name:'sossita'},
    { id: 7, name: 'chaparro'},
    { id: 23, name: 'ginna'}
 ];
 
 
 // Creamos la función para ordenas los elementos con sort
 socios.sort((manito, pepino) =>{
     return  manito.id - pepino.id
 })

console.log(socios);
