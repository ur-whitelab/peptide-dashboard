<template>
<div>
  <div v-if="prediction.found_motif">
    <h2>Found Motif: {{prediction.found_motif}}</h2>
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
      'most_likely_motif_idx': {type: Number, default: 0}
    }
  }
}
</script>
