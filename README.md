# CPU Cooler HID Display

Este projeto tem como objetivo monitorar a temperatura da CPU e exibi-la em um display conectado via um dispositivo HID. A temperatura da CPU é obtida utilizando o módulo `psutil` e é enviada periodicamente para o dispositivo através da comunicação HID. O script roda como um serviço, garantindo que ele seja iniciado automaticamente sempre que o sistema for reiniciado.

## Exemplo de Watercooler Compatível

Imagens meramente ilustrativas do tipo de hardware utilizado:

![Cooler 360mm](/imgs/Water Cooler Husky Glacier.jpeg)
![Cooler 240mm](/imgs/Water Cooler Husky Glacier-240.webp)

## Funcionalidades

- **Monitoramento da Temperatura da CPU**: O script usa a biblioteca `psutil` para obter a temperatura do processador (Tctl).
- **Comunicação HID**: A temperatura da CPU é enviada para um dispositivo HID para exibição em um display (por exemplo, um cooler com display).
- **Execução como Serviço**: O script roda como um serviço systemd, garantindo que ele seja executado automaticamente após reinicializações.

## Pré-requisitos

- Python 3.6 ou superior
- Biblioteca `psutil` para monitoramento da temperatura
- Biblioteca `hid` para comunicação com dispositivos HID
- Sistema Linux (testado em distribuições baseadas no Debian)

## Instalação

### 1. Clone o repositório:

```bash
git clone https://github.com/Guh-paixao/cpu-cooler-husky-linux.git
cd cpu-cooler
```

### 2. Instale as dependências:

```bash
pip install psutil hid
```

### 3. Torne o script executável:

```bash
sudo chmod +x /usr/local/bin/cpu_cooler.py
```

### 4. Configure o serviço systemd:

Crie o arquivo de serviço systemd:

```bash
sudo nano /etc/systemd/system/cpu-cooler.service
```

Adicione o seguinte conteúdo:

```ini
[Unit]
Description=CPU Cooler HID Display Service
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /usr/local/bin/cpu_cooler.py
Restart=always
User=root
StandardOutput=journal
StandardError=journal
Environment=PATH=/usr/bin:/usr/local/bin
WorkingDirectory=/usr/local/bin

[Install]
WantedBy=multi-user.target
```

### 5. Recarregue o systemd e inicie o serviço:

```bash
sudo systemctl daemon-reload
sudo systemctl enable cpu-cooler.service
sudo systemctl start cpu-cooler.service
```

### 6. Verifique o status do serviço:

```bash
sudo systemctl status cpu-cooler.service
```

### 7. Verifique os logs de execução:

```bash
sudo journalctl -u cpu-cooler.service
```

## Contribuindo

Se você quiser contribuir para este projeto, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
