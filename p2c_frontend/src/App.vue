<template>
  <v-app :dark="dark" >
    <v-navigation-drawer
        v-model="drawer"
        app
        clipped
      >
        <v-list dense right>
          <v-list-item
          v-for = "task in tasks" v-bind:key = "task.id" :to="'/'+ task.id"
          >
            <v-list-item-content >
                <v-list-item-title>{{task.id}} {{task.title}}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    <v-app-bar
        app
        clipped-left
        dense
      >
        <v-app-bar-nav-icon  @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <v-spacer></v-spacer>
      <v-tabs   right>
        <v-tab to="/"><b>Exercise</b></v-tab>
        <v-tab to="/compiler"><b>Compiler</b></v-tab>
      </v-tabs>
      </v-app-bar>
    <v-main >
        <v-container
          class="fill-height"
          fluid
        >
    <router-view/>
          <v-row
            align="center"
            justify="center"
          >
            <v-col class="shrink">
            </v-col>
          </v-row>
        </v-container>
      </v-main>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  data: () => ({
    drawer: false,
    mode: true,
    tasks: [],
  }),

  props: {
    source: String,
  },
  created() {
    axios.get('http://127.0.0.1:8000/api/tasks/')
      .then((response) => {
        this.tasks = response.data;
      });
  },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

</style>
