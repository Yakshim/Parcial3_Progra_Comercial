<template>
  <div>
    <ul>
        <li :key="huesped.id" v-for="huesped  in huespedes.data.allHuespedes" >
          {{huesped.id}}
          {{huesped.name}}
          {{huesped.direccion}}
          {{huesped.correo}}
          {{huesped.telefono}}
        </li>
    </ul>    
  </div>
</template>

    
<script>

import gql from 'graphql-tag'


  export default {
    name: 'HuespedsList',    
    //definimos la variable que almacenara el listado de ingredientes
    data () {
      return {
        huespedes: ''
      }
    },    

    //declaramos un metodo que vaya a leer los ingredientes a GraphQl

    methods:
    {
      // sera un funcion asincrona pues debera esperar hasta recibir la respuesta externa
      async leerHuespedes(){

        
       //desde aquí se realiza la consulta a Graphql y el resultado se guarda en una constante

        const huespedesGraphql = await this.$apollo.query({
        query: gql`query {
                   allHuespedes {
                      id
                      name
                      direccion
                      correo
                      telefono
                    }
                  }`,     
        })

        //El dato obtenido de Graphql se lo asignamos a la variable ingredientes que se mostrara en el template
        this.huespedes = huespedesGraphql
   
      }      


    },

    //el metodo leerIngredientes se ejecutara cada vez que los componentes de la pagina ya esten montados

    mounted () {

      this.leerHuespedes()

    }

    

  }

  

</script>