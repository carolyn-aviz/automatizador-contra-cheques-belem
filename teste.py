from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do ChromeDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\Carolyn\Downloads",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 60)

driver.get("https://sistemas.belem.pa.gov.br/portaldoservidor/#/login")

# Login
matricula_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Matrícula']")))
matricula_input.send_keys("1859200")

senha_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Senha']")))
senha_input.send_keys("Ben10")

entrar_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Entrar')]")))
entrar_btn.click()

# Acessar área de contracheque
botao_contracheque = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//div[h2[contains(text(),'Contra Cheque')]]//button[contains(text(),'Acesse')]"
)))

driver.execute_script("arguments[0].click();", botao_contracheque)

def esperar_carregamento_sumir(driver, timeout=15):
    try:
        WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "cinbesa-loading-container"))
        )
    except:
        print("⚠️ Timeout esperando o carregamento sumir.")

def abrir_dropdown_por_id(dropdown_id):
    esperar_carregamento_sumir(driver)  # <-- espera o overlay de loading sumir
    dropdown_trigger = wait.until(EC.element_to_be_clickable((
        By.XPATH, f"//p-dropdown[@id='{dropdown_id}']//div[contains(@class,'p-dropdown-trigger')]"
    )))
    dropdown_trigger.click()

# Coletar anos
abrir_dropdown_por_id("ano")
anos = wait.until(EC.presence_of_all_elements_located((
    By.XPATH, "//div[contains(@class,'p-dropdown-items-wrapper')]//li/span"
)))
anos_textos = [ano.text.strip() for ano in anos if ano.text.strip()]
abrir_dropdown_por_id("ano")  # fecha dropdown

print(f"Anos encontrados: {anos_textos}")

# Loop pelos anos
for ano in anos_textos:
    print(f"\nProcessando ano: {ano}")
    abrir_dropdown_por_id("ano")
    wait.until(EC.element_to_be_clickable((
        By.XPATH, f"//li//span[normalize-space(text())='{ano}']"
    ))).click()
    time.sleep(2)

    # Meses
    abrir_dropdown_por_id("mes")
    meses = wait.until(EC.presence_of_all_elements_located((
        By.XPATH, "//div[contains(@class,'p-dropdown-items-wrapper')]//li/span"
    )))
    meses_textos = [mes.text.strip() for mes in meses if mes.text.strip()]
    abrir_dropdown_por_id("mes")

    print(f"Meses encontrados para {ano}: {meses_textos}")

    for mes in meses_textos:
        print(f"\nProcessando mês: {mes}")
        try:
            abrir_dropdown_por_id("mes")
            wait.until(EC.element_to_be_clickable((
                By.XPATH, f"//li//span[normalize-space(text())='{mes}']"
            ))).click()
            time.sleep(2)

            # Contratos
            abrir_dropdown_por_id("contrato")
            contratos = wait.until(EC.presence_of_all_elements_located((
                By.XPATH, "//div[contains(@class,'p-dropdown-items-wrapper')]//li/span"
            )))
            contratos_textos = [c.text.strip() for c in contratos if c.text.strip()]
            abrir_dropdown_por_id("contrato")

            print(f"Contratos encontrados para {mes}/{ano}: {contratos_textos}")

            for contrato in contratos_textos:
                print(f"Processando contrato: {contrato}")
                try:
                    abrir_dropdown_por_id("contrato")
                    wait.until(EC.element_to_be_clickable((
                        By.XPATH, f"//li//span[normalize-space(text())='{contrato}']"
                    ))).click()
                    time.sleep(1)

                    # Botão Gerar Contra-Cheque
                    gerar_btn = wait.until(EC.element_to_be_clickable((
                        By.XPATH, "//button[span[contains(text(),'Gerar Contra-Cheque')]]"
                    )))
                    gerar_btn.click()

                    time.sleep(5)  # tempo para download
                    print(f"✅ Baixado: {ano} - {mes} - {contrato}")

                except Exception as e:
                    print(f"⚠️ Erro no contrato {contrato} ({mes}/{ano}): {str(e)}")
                    continue

        except Exception as e:
            print(f"⚠️ Erro no mês {mes} de {ano}: {str(e)}")
            continue

driver.quit()
