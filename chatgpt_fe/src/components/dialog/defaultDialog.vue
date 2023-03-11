<template>
  <div class="mainContent">
    <Dialg></Dialg>
    <InputDialg></InputDialg>
  </div>
</template>
<script setup>
import InputDialg from "./dialogItem/inputDialog.vue"
import Dialg from "./dialogItem/userDialog.vue"
</script>
<style scoped>
 .mainContent{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  height: 100%;
 }
</style>