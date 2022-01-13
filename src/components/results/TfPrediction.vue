<template>
  <div>
    <tf-result
      id="sol-predict"
      title="sol"
      description="Prediction of solubility"
      v-bind:prediction="prediction.sol"
      v-bind:sequence="sequence"
      v-bind:name="prediction.sol.predict ? 'Soluble' : 'Not soluble.'"
    />
    <hr />
    <model-card :url="this.url + '/card.json'"> </model-card>
  </div>
</template>

<script>
import TfResult from "./TfResult";
import getModel from "../lib/rnn";
import ModelCard from "./ModelCard.vue";
import _ from "lodash";
export default {
  name: "TfPrediction",
  components: { TfResult, ModelCard },
  props: {
    sequence: String,
    url: String,
    width: {
      type: Number,
      default: 300,
    },
  },
  data() {
    return {
      status: "loading",
      rnn: null,
    };
  },
  mounted: function () {
    this.rnn = getModel();
    this.rnn.startLoad(this.url + "model.json");
  },
  data: function () {
    return {
      prediction: { sol: { predict: null }, finished: false },
    };
  },
  watch: {
    sequence: _.debounce(function () {
      this.makePrediction(this.sequence);
    }, 1000),
  },
  methods: {
    makePrediction: async function (str) {
      this.status = this.rnn.model_loaded;
      if (str.length >= 3 && this.status === "loaded") {
        const x = this.rnn.seq2vec(str);
        const yhat = await this.rnn.model(x).array();
        if (yhat) {
          this.prediction.sol.score = yhat;
          this.prediction.sol.predict = true ? yhat > 0 : false;
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




