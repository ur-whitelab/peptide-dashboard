<template>
  <div class="prediction-table">
    <table
      class="table"
      :class="{
        'has-background-success': ready && prediction.predict,
        'has-background-warning': ready && !prediction.predict,
        'has-background-grey': !ready,
      }"
    >
      <tr>
        <td>Predicted activity?</td>
        <td class="rightalign">{{ display }}</td>
      </tr>
      <tr title="Fraction of cutoff likelihood.">
        <td>Probability of Active:</td>
        <td class="rightalign">
          {{ score }}
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: "TfResult",
  props: {
    prediction: {
      accuracy: { type: Number, default: 0.0 },
      predict: { type: Boolean, default: false },
      score: { type: Number, default: 0.0 },
    },
    ready: Boolean,
    title: String,
  },
  computed: {
    display: function () {
      if (this.ready && this.prediction.predict) return "Yes";
      if (this.ready && !this.prediction.predict) return "No.";
      return "...";
    },
    score: function () {
      if (this.ready) return parseFloat(this.prediction.score).toFixed(2);
      return "...";
    },
  },
};
</script>

<style lang="scss">
.rightalign {
  text-align: right;
}
.uppercase {
  text-transform: uppercase;
}
.prediction-table {
  overflow-x: auto;
}
</style>
