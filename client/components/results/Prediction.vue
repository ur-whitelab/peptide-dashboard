<template>
    <div>
      <prediction-result title="antimicrobial" description="Prediciton of antimicrobial activity" v-bind:prediction=prediction.antimicrobial> </prediction-result>
      <prediction-result title="antifouling" description="Prediciton of antimicrobial activity" v-bind:prediction=prediction.antifouling> </prediction-result>
    </div>
</template>

<script>
import PredictionResult from './PredictionResult'
import axios from 'axios'
export default {
  name: 'Prediction',
  components: { PredictionResult },
  props: {
    sequence: String,
    port: String,
    host: {
      default: '127.0.0.1'
    },
    width: {
      type: Number,
      default: 300
    }
  },
  data () {
    return {
      prediction: {'antifouling': {}, 'antimicrobial': {}}
    }
  },
  watch: {
    sequence: function () {
      this.makePrediction(this.sequence)
    }
  },
  methods: {
    makePrediction: async function (str) {
      if (str.length >= 3) {
        const response = await axios.get('http://' + this.host + ':' + this.port + '/predict/' + str)
        if ('prediction' in response.data) {
          this.prediction.antifouling = response.data.prediction.antifouling
          this.prediction.antimicrobial = response.data.prediction.antimicrobial
        }
      }
    }
  }
}
</script>
