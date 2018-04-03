<template>
  <div>
    <h4> Input</h4>
    <input v-model='query'>
    <br>
    <ol>
      <li v-for="p in prediction"> {{ p }} </li>
    </ol>
  </div>
</template>

<script>
  import axios from 'axios'
  import _ from 'lodash'

  export default{
    name: 'linked-input-box',
    props: {
      port: {
        default: '5000',
        type: String
      },
      host: {
        default: 'localhost',
        type: String
      },
      width: {
        default: '100',
        type: String
      }
    },
    data () {
      return {
        query: '',
        prediction: ''
      }
    },
    watch: {
      query: function () {
        this.updatePrediction()
      }
    },
    methods: {
      updatePrediction: _.throttle(async function () {
        try {
          const response = await axios.get('http://' + this.host + ':' + this.port + '/predict/' + this.query)
          if ('prediction' in response.data)
            this.prediction = response.data.prediction
        } catch (err) {
          // pass
        }
      }, 250)
    }
  }
</script>