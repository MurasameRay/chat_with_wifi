<template>
  <div class="inputText">
    <el-input
      v-model="text"
      :rows="2"
      type="textarea"
      placeholder="Please input"
      clearable
      @keyup.enter="enterKey"
    />
  </div>
  <!-- <audio ref="audio">
    <source src="" >
  </audio> -->
</template>
<script setup>
  import {getVoice} from '../../../request/api/voice'
  import { ref } from 'vue'
  const text = ref('')
  const audio = ref(null)
  async function enterKey() {
    let res = await getVoice(text.value)
    console.log(res);
  }
</script>
<style scoped>
  .inputText{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 10%;
  }
  .el-textarea{
    width: 40%;
    box-shadow: 1px 1px 10px #CDD0D6,
                -1px -1px 10px #CDD0D6;
  }
</style>