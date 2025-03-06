import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    target: 'esnext',
  },
  server: {
    port: 3000, // Cambia el puerto a 3000 o cualquier otro que prefieras
  }
})