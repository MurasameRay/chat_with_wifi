<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="15%">
          <el-button 
            color="#303133"
            class="elbutton" 
            size="large" 
            @click="addNewTab()"
          >
            <svg class="icon" aria-hidden="true">
              <use xlink:href="#icon-tianjia1"></use>
            </svg>
            <span>New chat</span>
          </el-button>
          <div class="elMenu">
            <el-menu
              active-text-color="#FFFFFF"
              background-color="#303133"
              default-active="/defaultChat"
              text-color="#fff"
              class="el-menu-vertical-demo"
              router
            >
              <!-- <el-menu-item index="/defaultChat">
                <svg class="icon" aria-hidden="true">
                  <use xlink:href="#icon-jianyi"></use>
                </svg>
                <span>Algorithm Testing Tool.</span>
              </el-menu-item> -->
              <el-menu-item v-for="item in newChat" :key="item" index="/defaultChat">
                <svg class="icon" aria-hidden="true">
                  <use xlink:href="#icon-jianyi"></use>
                </svg>
                <span>{{ item.name }}</span>
                <svg class="icon" aria-hidden="true">
                  <use xlink:href="#icon-shanchu"></use>
                </svg>
              </el-menu-item>
            </el-menu>
          </div>
      </el-aside>
      <el-main><router-view></router-view></el-main>
    </el-container>
  </div>
    
  </template>
  <script setup>
  import { ref,reactive } from 'vue'
  const newRouter = reactive([
    "/defaultChat"
  ])
  const newChat = reactive([{
    name: "Algorithm Testing Tool."
  }])
  const addNewTab = () =>{
    newChat.push({
      name:"New chat"
    })
    
    newRouter.push("")
  }
  
  </script>
  <style scoped>
  .el-menu{
    border-right: none
  }
  .el-aside {
    position: absolute;
    background-color: #303133;
    height: 100%;
    top: 0;
    left: 0;
  }
  .el-main{
    position: absolute;
    height: 100%;
    width: 85%;
    left: 15%;
    top: 0;
  }
  .elbutton {
    border-color: #A8ABB2;
    margin-bottom: 2%;
    width: 90%;
    margin-left: 0.6rem;
    margin-top: 1rem;
    margin-bottom: 0.8rem;
  }
  .elbutton span {
    margin-left: 0.5em;
  }
  .el-menu-item span{
    margin: auto 0.5rem;
  }
  .icon {
    width: 1.3rem;
    height: 1.3rem;
    fill: white;
  }
  </style>