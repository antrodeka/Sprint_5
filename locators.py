REG_BUTTON = '//button[text()="Зарегистрироваться"]'  # Кнопка "Зарегистрироваться" на главной странице
PERSONAL_ACCOUNT = '//p[text()="Личный Кабинет"]'  # Личный Кабинет
LOGIN_IN_ACCOUNT = '//button[text()="Войти в аккаунт"]'  # Кнопка "Войти в аккаунт"
LOGIN_EMAIL = "//input[@type='text']"  # Поле для логина на странице входа
LOGIN_PASSWORD = ".//input[@type='password']"  # Поле для пароля на странице входа
LOGIN_BUTTON = '//button[contains(text(), "Войти")]'  # Кнопка "Войти" на странице входа
LOGOUT_BUTTON = '//button[text()="Выход"]'  # Кнопка "Выйти" в Личном Кабинете
RESTORE_PASSWORD_BUTTON = '//a[contains(text(), "Восстановить пароль")]'  # Кнопка "Восстановить пароль" на странице входа
RESET_PASSWORD_LOGIN_BUTTON = "//a[@href='/login']" # Кнопка "Войти" на странице сброса пароля
LOGIN_BUTTON_ON_PAGES = '//a[contains(text(), "Войти")]'  # Кнопка "Войти" на странице регистрации
REG_BUTTON_ON_AUTH_PAGE = '//a[contains(text(), "Зарегистрироваться")]' # Кнопка "Зарегистрироваться" на странице авторизации
REG_NAME_INPUT = '//label[text()="Имя"]/following-sibling::input'  # Поле для ввода имени
REG_EMAIL_INPUT = '//label[text()="Email"]/following-sibling::input'  # Поле для ввода E-mail
REG_PASSWORD_INPUT = 'Пароль' # Поле для ввода пароля
ERROR_PASS_MESSAGE = '//p[text()="Некорректный пароль"]'  # Некорректный пароль
BUN_BUTTON = '//span[text()="Булки"]/parent::div'  # Кнопка "Булки"
SAUCE_BUTTON = '//span[text()="Соусы"]/parent::div'  # Кнопка "Соусы"
STUFF_BUTTON = '//span[text()="Начинки"]/parent::div'  # Кнопка "Начинка"
LOGO_STELLAR_BURGERS = "//div[contains(@class,'logo')]"  # Логотип сайта
CONSTRUCTOR_BUTTON = "//p[text()='Конструктор']"  # Кнопка "Конструктор"
ORDER_BUTTON = "//button[text()='Оформить заказ']" # Кнопка "Оформить заказ" на главной странице
