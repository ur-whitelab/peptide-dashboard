<template>
  <div>
    <p><small>Reference: <a :href="reflink">{{reftitle}}</a>. <em>{{journal ? journal : ''}}</em> <b>{{year ? ', ' + year : ''}}</b><em>{{volume ? ',' + volume : ''}}</em> {{issue ? '(' + issue + ')' : ''}} {{pages ? pages +'.' : '.' }} {{doi ? 'DOI: ' + doi + '.' : ''}}</small></p>
  </div>
</template>

<script>
export default {
  name: 'Reference',
  props: {
    reflink: {type: String, default: ''},
    reftitle: {type: String, default: ''},
    journal: {type: String, default: ''},
    year: {type: String, default: ''},
    issue: {type: String, default: ''},
    volume: {type: String, default: ''},
    pages: {type: String, default: ''},
    doi: {type: String, default: ''}
  }
}
</script>
