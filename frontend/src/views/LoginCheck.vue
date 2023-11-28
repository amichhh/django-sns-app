<template>
  <v-container grid-list-md>
    <v-layout row wrap align-center justify-center fill-height>
      <v-flex xs12 sm8 lg4 md5>
        <v-card class="login-card">
          <v-card-title>
            <span class="headline">Login to HedgeHogs</span>
          </v-card-title>

          <v-spacer />

          <v-card-text>

            <v-layout row fill-height justify-center align-center v-if="loading">
              <v-progress-circular :size="50" color="primary" indeterminate />
            </v-layout>


            <v-form v-else ref="form" v-model="valid" lazy-validation>
              <v-container>

                <v-text-field v-model="param.username" :counter="70" label="ユーザー名" :rules="rules.username"
                  maxlength="70" required />

                <v-text-field type="password" v-model="param.password" :counter="20" label="パスワード"
                  :rules="rules.password" maxlength="20" required />

              </v-container>
              <v-btn class="pink white--text" :disabled="!valid" @click="login">Login</v-btn>

            </v-form>


          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script setup lang="ts">
import axios from 'axios';
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()

interface LoginParam {
  username: string,
  password: string
}

const param: LoginParam = reactive({
  username: "",
  password: "",
})
const valid = ref(true)
const loading = ref(false)
const rules = {
  username: [
    (v: any) => !!v || "ユーザー名は必須です",
    (v: any) => (v && v.length > 4) || "ユーザー名は5文字以上でなければなりません",
    (v: any) => /^[a-z0-9_]+$/.test(v) || "許可されていない文字が入力されています"
  ],
  password: [
    (v: any) => !!v || "パスワードは必須です",
    (v: any) => (v && v.length > 4) || "ユーザー名は5文字以上でなければなりません"
  ]
}

const login = () => {
  loading.value = true
  console.log(param)
  axios.post('http://localhost:8000/auth/', param )
    .then(response => {
      console.log("success!")
      console.log(response.data.token)
      // $session.start()
      // this.$session.set('token', response.data.token);
      router.push('/messages')
    }).catch(error => {
      console.log("error!")
      loading.value = false
      console.log(error)
    })
}
  

</script>