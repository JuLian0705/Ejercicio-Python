import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  vus: 1000, // usuarios virtuales
  duration: '30s', // tiempo de prueba
};

export default function () {
  http.get('https://tusitioenetlify.netlify.app');
  sleep(1);
}
