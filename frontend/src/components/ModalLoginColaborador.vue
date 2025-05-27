<template>
  <Dialog
    v-model:visible="modelVisible"
    modal
    appendTo="body"
    :style="{ width: '400px', height: '600px' }"
    :pt="ptDialog">
    <div class="login-container">
      <h2 class="login-title">Registro de Ponto</h2>

      <div class="form-group">
        <label for="cpf">CPF</label>
        <InputMask id="cpf" v-model="cpf" mask="999.999.999-99" class="login-input" />
      </div>

      <div class="form-group">
        <label for="senha">Senha</label>
        <Password v-model="senha" inputId="senha" toggleMask class="login-input" />
      </div>

      <Button label="Registrar Ponto" class="login-button" @click="handleLogin" :disabled="!formularioValido" />

      <!-- <Message v-if="erro" severity="error" class="login-msg">{{ erro }}</Message>
      <Message v-if="sucesso" severity="success" class="login-msg">Login realizado com sucesso!</Message> -->
    </div>
  </Dialog>
  <Dialog
    v-model:visible="mostrarResultado"
    modal
    class="dialog-resultado"
    :style="{ width: '400px', height: '600px' }"
    :pt="ptDialog">
  <div class="msg-container">
    <h3 class="rgt-title">Registro de Ponto</h3>
    <RelogioDigital />
    <div class="msg-container-parag">
        <p>{{ mensagem }}</p>
    </div>
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
import { loginColaborador, registrarPonto } from '@/services/api'
import RelogioDigital from "./RelogioDigital.vue";


const colaborador = ref(null)
const mensagem = ref('')
const mostrarResultado = ref(false)

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
// const erro = ref('')
// const sucesso = ref(false)

const formularioValido = computed(() => cpf.value.replace(/\D/g, '').length === 11 && senha.value.trim().length >= 4)

async function handleLogin() {
  try {
    const response = await loginColaborador(cpf.value, senha.value)

    // Corrige: pega os dados reais da resposta
    colaborador.value = response 

    // Logs para depuração
    console.log('Colaborador autenticado:', colaborador.value)
    console.log('Enviando para registrar ponto com ID:', colaborador.value.id_col)

    const registro = await registrarPonto(colaborador.value.id_col)

    const hora = new Date(registro.timestamp_reg).toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' })

    mensagem.value = `${colaborador.value.nome_col}, seu ponto de ${registro.tipo_reg} foi registrado às ${hora}`
    mostrarResultado.value = true

    // (opcional) Limpa os campos
    cpf.value = ''
    senha.value = ''
  } catch (error: any) {
    console.error('Erro no login ou registro de ponto:', error)

    if (error.response) {
      console.log('Status:', error.response.status)
      console.log('Data:', error.response.data)
    }

    mensagem.value = '❌ Erro ao registrar ponto. Verifique CPF e senha.'
    mostrarResultado.value = true
    console.log(colaborador.value)
  }
}

</script>

<style>
.dialog-resultado .p-dialog-content {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>

<style scoped>

.login-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  padding: 1rem;
}

.msg-container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  padding: 1rem;
  gap: 2rem;
  width: fit-content;
}

.msg-container-parag {
  justify-content: center;
  font-family: Arial;
}

.login-title {
  text-align: center;
  font-size: 3rem;
  font-weight: bold;
  font-family: Arial;
  margin-bottom: 0.5rem;
}

.rgt-title {
  text-align: center;
  font-size: 2rem;
  font-weight: bold;
  font-family: Arial;
  margin-bottom: 0rem;
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
