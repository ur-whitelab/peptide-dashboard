<template>
  <small
    ><a :href="reflink">{{ reftitle }}</a
    >. <em>{{ journal ? journal : "" }}</em
    ><span v-if="year"
      >, <b>{{ year ? year : "" }}</b></span
    ><em>{{ volume ? ", " + volume : "" }}</em
    >{{ issue ? " (" + issue + ")" : "" }}{{ pages ? " " + pages + "." : "." }}
    {{ doi ? "DOI: " + doi + "." : "" }}</small
  >
</template>

<script>
export default {
  name: "Reference",
  props: {
    reflink: { type: String, default: "" },
    reftitle: { type: String, default: "" },
    journal: { type: String, default: "" },
    year: { type: String, default: "" },
    issue: { type: String, default: "" },
    volume: { type: String, default: "" },
    pages: { type: String, default: "" },
    doi: { type: String, default: "" },
  },
};
</script>
