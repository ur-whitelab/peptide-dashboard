<template>
  <div class="tf-prediction">
    <tf-result
      title="sol"
      description="Prediction of solubility"
      v-bind:prediction="prediction"
      v-bind:ready="prediction.finished"
      :adjective="adjective"
    />
    <br />
    <model-card :url="this.url + '/card.json'"> </model-card>
  </div>
</template>

<style>
</style>

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
    adjective: String,
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
      prediction: { score: null, predict: false, finished: false },
    };
  },
  watch: {
    sequence: function (new_value) {
      this.prediction.finished = false;
      this.$emit(this.adjective + "-update", null);
      this.debouncedPredict(new_value);
    },
  },
  methods: {
    predict: async function (str) {
      this.status = this.rnn.model_loaded;
      if (str.length >= 1 && this.status === "loaded") {
        const x = this.rnn.seq2vec(str);
        const yhat = await this.rnn.model(x).array();
        if (yhat) {
          this.prediction.score = yhat;
          this.prediction.predict = yhat > 0.5;
          this.prediction.finished = true;
          this.$emit(
            this.adjective + "-update",
            parseFloat(yhat * 100).toFixed(0) + "%"
          );
        } else {
          this.prediction.score = null;
          this.prediction.predict = false;
          this.prediction.finished = false;
        }
      }
    },
  },
};
</script>




