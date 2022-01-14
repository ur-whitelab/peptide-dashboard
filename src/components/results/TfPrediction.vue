<template>
  <div>
    <tf-result
      title="sol"
      description="Prediction of solubility"
      v-bind:prediction="prediction.sol"
      v-bind:ready="this.prediction.finished"
    />
    <hr />
    <model-card :url="this.url + '/card.json'"> </model-card>
  </div>
</template>

<script>
import TfResult from "./TfResult";
import getModel from "../lib/tf-models";
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
  created: function () {
    this.debouncedPredict = _.debounce(this.predict, 1000);
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
    sequence: function (new_value) {
      this.debouncedPredict(new_value);
    },
  },
  methods: {
    predict: async function (str) {
      console.log("Starting in model " + this.url);
      this.status = this.rnn.model_loaded;
      if (str.length >= 1 && this.status === "loaded") {
        const x = this.rnn.seq2vec(str);
        const yhat = await this.rnn.model(x).array();
        if (yhat) {
          this.prediction.sol.score = yhat;
          this.prediction.sol.predict = true ? yhat > 0.5 : false;
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




