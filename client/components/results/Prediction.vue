<template>
<div>
  <h3 ><em>{{sequence ? 'Antimicrobial Model' : ''}}</em></h3>
  <prediction-result id="antimicrobial-predict" title="antimicrobial" description="Prediciton of antimicrobial activity" v-bind:prediction=prediction.antimicrobial v-bind:sequence="sequence" :name="prediction.antimicrobial.predict? 'Antimicrobial activity predicted.' : 'No antimicrobial activity predicted.'"></prediction-result>
  <br>
  <h3 ><em>{{sequence ? 'Antifouling Model' : ''}}</em></h3>
  <prediction-result id="antifouling-predict" title="antifouling" description="Prediciton of antifouling activity" v-bind:prediction=prediction.antifouling v-bind:sequence="sequence" :name="prediction.antifouling.predict? 'Antifouling activity predicted.' : 'No antifouling activity predicted.'"> </prediction-result>
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
  data: function () {
    return {
      prediction: {'antifouling': {}, 'antimicrobial': {}, 'finished': false}
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
        const response = await axios.get(this.host + (this.port ? ':' + this.port : '') + '/predict/' + str)
        if ('prediction' in response.data) {
          this.prediction.antifouling = response.data.prediction.antifouling
          this.prediction.antimicrobial = response.data.prediction.antimicrobial
          this.prediction.finished = true
        } else {
          this.prediction.antifouling = {}
          this.prediction.antimicrobial = {}
          this.prediction.finished = false
        }
      }
    }
  }
}
</script>




