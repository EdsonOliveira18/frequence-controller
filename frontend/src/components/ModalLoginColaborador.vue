<template>
  <Dialog
    v-model:visible="modelVisible"
    modal
    appendTo="body"
    :style="{ width: '350px', height: '500px' }"
    :pt="ptDialog">
    <div class="login-container">
      <h2 class="login-title">Login</h2>

      <div class="form-group">
        <label for="cpf">CPF</label>
        <InputMask id="cpf" v-model="cpf" mask="999.999.999-99" class="login-input" />
      </div>

      <div class="form-group">
        <label for="senha">Senha</label>
        <Password v-model="senha" inputId="senha" toggleMask class="login-input" />
      </div>

      <Button label="Entrar" class="login-button" @click="fazerLogin" :disabled="!formularioValido" />

      <Message v-if="erro" severity="error" class="login-msg">{{ erro }}</Message>
      <Message v-if="sucesso" severity="success" class="login-msg">Login realizado com sucesso!</Message>
    </div>
  </Dialog>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, computed, ref } from 'vue'
import Dialog from 'primevue/dialog'
import InputMask from 'primevue/inputmask'
import Password from 'primevue/password'
import Button from 'primevue/button'
import Message from 'primevue/message'
import { loginColaborador } from '@/services/api'

const props = defineProps<{ visible: boolean }>()
const emit = defineEmits<{
  (e: 'update:visible', value: boolean): void
}>()

const ptDialog = {
  header: {
    style: 'padding-top: 1rem; padding-bottom: 0; padding-left: 1rem; padding-right: 1rem; display: flex; justify-content: flex-end;'
  }
};

const modelVisible = computed({
  get: () => props.visible,
  set: (value) => emit('update:visible', value),
})

const cpf = ref('')
const senha = ref('')
const erro = ref('')
const sucesso = ref(false)

const formularioValido = computed(() => cpf.value.replace(/\D/g, '').length === 11 && senha.value.trim().length >= 4)

const fazerLogin = async () => {
  erro.value = ''
  sucesso.value = false
  try {
    const resposta = await loginColaborador({
      cpf: cpf.value.replace(/\D/g, ''),
      senha: senha.value
    })
    sucesso.value = true
    setTimeout(() => {
      alert("⚡ Login bem-sucedido. Em breve iniciaremos o registro de ponto.")
    }, 1000)
  } catch (e: any) {
    erro.value = e?.response?.data?.detail || 'Erro ao realizar login.'
  }
}
</script>

<style scoped>

.login-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  padding: 1rem;
}

.login-title {
  text-align: center;
  font-size: 3rem;
  font-weight: bold;
  font-family: Arial;
  margin-bottom: 0.5rem;
}

.form-group {
  font-family: Arial;
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.login-input {
  width: 100%;
}

.login-button {
  font-family: Arial;
  width: 100%;
  margin-top: 1rem;
  background-color: #17a2b8;
  border: none;
}

.login-msg {
  margin-top: 1rem;
  text-align: center;
}

</style>
