<template>
  <div class="prediction-table">
    <table
      class="table"
      :class="{
        'has-background-primary': ready && prediction.predict,
        'has-background-warning': ready && !prediction.predict,
        'has-background-white-ter': !ready,
      }"
    >
      <tbody>
        <tr>
          <td class="has-text-right">{{ display }}</td>
          <td class="has-text-left">
            {{
              ready
                ? adjective
                : "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
            }}
          </td>
        </tr>
        <tr title="probability">
          <td class="has-text-right">{{ score }}&nbsp;</td>
          <td class="has-text-left"><span v-if="ready">probability</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "TfResult",
  props: {
    prediction: {
      predict: { type: Boolean, default: false },
      score: { type: Number, default: 0.0 },
    },
    ready: Boolean,
    title: String,
    adjective: String,
  },
  computed: {
    display: function () {
      if (this.ready) {
        if (this.prediction.score >= 0.9) return "is";
        if (this.prediction.score >= 0.7) return "likely";
        if (this.prediction.score >= 0.4) return "weakly";
        if (this.prediction.score >= 0.1) return "unlikely";
        return "not";
      }
      return "";
    },
    score: function () {
      if (this.ready)
        return parseFloat(this.prediction.score * 100).toFixed(0) + "%";
      return " ";
    },
  },
};
</script>

<style lang="scss">
.uppercase {
  text-transform: uppercase;
}
.prediction-table {
  overflow-x: auto;
}
</style>
