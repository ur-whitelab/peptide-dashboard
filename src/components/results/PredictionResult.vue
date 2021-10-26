<template>
  <div class="prediction-table">
    <table v-if="sequence" class="table">
      <tr title="Accuracy on withheld data.">
        <td>Model accuracy:</td>
        <td class="rightalign">{{ prediction.accuracy }}</td>
      </tr>
      <tr
        v-if="prediction.found_motif"
        title="Found motif displayed in bold green."
      >
        <td>Found Motif:</td>
        <td class="rightalign">
          <font class="uppercase"
            >{{ displayed_sequence.left
            }}<strong
              ><font color="green">{{
                displayed_sequence.middle
              }}</font></strong
            >{{ displayed_sequence.right }}</font
          >
        </td>
      </tr>
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
      <tr
        :title="
          prediction.qspr_contributes_more
            ? 'The QSPR half of this model contributed more likelihood than the motif half.'
            : 'The motif half of this model contributed more likelihood than the QSPR half.'
        "
      >
        <td>Greater contribution:</td>
        <td class="rightalign">
          {{ prediction.qspr_contributes_more ? "QSPR" : "Motif" }}
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: "PredictionResult",
  props: {
    prediction: {
      accuracy: { type: Number, default: 0.0 },
      predict: { type: Boolean, default: false },
      qspr_contributes_more: { type: Boolean, default: false },
      found_motif: { type: String, default: "" },
      most_likely_motif: { type: String, default: "" },
      most_likely_motif_idx: { type: Number, default: 0 },
      most_likely_motif_start: { type: Number, default: 0 },
      score: { type: Number, default: 0.0 },
    },
    sequence: String,
    name: String,
  },
  computed: {
    displayed_sequence: function () {
      let result = { left: "", middle: "", right: "" };
      if (this.prediction.most_likely_motif_start > 10)
        result.left =
          "..." +
          this.sequence.slice(
            this.prediction.most_likely_motif_start - 4,
            this.prediction.most_likely_motif_start
          );
      else
        result.left = this.sequence.slice(
          0,
          this.prediction.most_likely_motif_start
        );
      result.middle = this.sequence.slice(
        this.prediction.most_likely_motif_start,
        this.prediction.most_likely_motif_start + 3
      );
      if (
        this.sequence.length - this.prediction.most_likely_motif_start - 3 >
        10
      )
        result.right =
          this.sequence.slice(
            this.prediction.most_likely_motif_start + 3,
            this.prediction.most_likely_motif_start + 7
          ) + "...";
      else
        result.right = this.sequence.slice(
          this.prediction.most_likely_motif_start + 3,
          this.sequence.length
        );
      return result;
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
