<template>
  <div>
    <h3>
      <em>{{ sequence ? "Solubility Model" : "" }}</em>
    </h3>
    <prediction-result
      id="sol-predict"
      title="sol"
      description="Prediciton of solubility"
      v-bind:prediction="prediction.sol"
      v-bind:sequence="sequence"
      :name="
        prediction.sol.predict
          ? 'Soluble'
          : 'Not soluble.'
      "
    >
    <p>{{status}}</p>
  </div>
</template>

<script>
import TFResult from "./TFResult";
import rnn from "../lib/rnn";
export default {
  name: "TFPrediction",
  components: { TFResult },
  props: {
    sequence: String,
    status: String,
    width: {
      type: Number,
      default: 300,
    },
  },
  mounted: function () {
    rnn.startLoad();
    this.status = "loading";
  },
  data: function () {
    return {
      prediction: { sol: {}, finished: false },
    };
  },
  watch: {
    sequence: function () {
      this.makePrediction(this.sequence);
    },
  },
  methods: {
    makePrediction: async function (str) {
      this.status = rnn.model_loaded;
      if (str.length >= 3 && this.status === 'loaded') {
        const x = rnn.seq2vec(str);
        const yhat = await rnn.model(x).array();
        if (yhat) {
          this.prediction.sol.score = yhat;
          this.predictions.sol.predict = true ? yhat > 0 : false;
          this.prediction.finished = true;
        } else {
          this.prediction.sol = {};
          this.prediction.finished = false;
        }
      }
    },
  },
};
</script>




