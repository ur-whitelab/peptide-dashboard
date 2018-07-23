<template>
<div>
  <div v-if="sequence">
    <h2 title="Accuracy on withheld data.">Model accuracy: {{prediction.accuracy}}</h2>
    <div v-if="prediction.found_motif">
      <h2 title="Found motif displayed in bold green.">Found Motif: <font class="uppercase">{{sequence.slice(0, prediction.most_likely_motif_start)}}<strong><font color="green">{{sequence.slice(prediction.most_likely_motif_start, prediction.most_likely_motif_start + 3)}}</font></strong>{{sequence.slice(prediction.most_likely_motif_start + 3, sequence.length)}}</font></h2>
    </div>
    <h2 :title="name">Predicted activity? {{prediction.predict ? 'Yes.' : 'No.'}}</h2>
    <h2 title="Fraction of cutoff likelihood.">Score: {{ parseFloat(prediction.score).toFixed(2)}}</h2>
    <h2 title="">The {{prediction.qspr_contributes_more ? 'QSPR' : 'motif'}} half of this model contributed more likelihood than the {{prediction.qspr_contributes_more ? 'motif' : 'QSPR'}} half.</h2>
  </div>
</div>
</template>

<script>
export default {
  name: 'PredictionResult',
  props: {
    prediction: {
      'accuracy': {type: Number, default: 0.0},
      'predict': {type: Boolean, default: false},
      'qspr_contributes_more': {type: Boolean, default: false},
      'found_motif': {type: String, default: ''},
      'most_likely_motif': {type: String, default: ''},
      'most_likely_motif_idx': {type: Number, default: 0},
      'most_likely_motif_start': {type: Number, default: 0},
      'score': {type: Number, default: 0.0}
    },
    sequence: String,
    name: String
  }
}
</script>

<style lang="scss">
  .uppercase { text-transform: uppercase; }
</style>
