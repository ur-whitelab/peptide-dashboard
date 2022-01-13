<template>
  <div class="prediction-table">
    <table v-if="sequence" class="table">
      <tr :title="name">
        <td>Predicted activity?</td>
        <td class="rightalign">{{ prediction.predict ? "Yes." : "No." }}</td>
      </tr>
      <tr title="Fraction of cutoff likelihood.">
        <td>Probability of Active:</td>
        <td class="rightalign">
          {{ parseFloat(prediction.score).toFixed(2) }}
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
    sequence: String,
    name: String,
    title: String,
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
