<template>
  <div>
    <h3>
      <em>{{ sequence ? "Solubility Model" : "" }}</em>
    </h3>
    <tf-result
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
import TfResult from "./TfResult";
import rnn from "../lib/rnn";
export default {
  name: "TfPrediction",
  components: { TfResult },
  props: {
    sequence: String,
    width: {
      type: Number,
      default: 300,
    },
  },
  data() {
    return {
      status: "loading",
    };
  },
  mounted: function () {
    rnn.startLoad();
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
      if (str.length >= 3 && this.status === "loaded") {
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




