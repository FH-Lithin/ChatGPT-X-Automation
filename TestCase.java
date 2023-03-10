

public class Test1 {

WebDriver driver;

@BeforeMethod

public void setUp() {

System.setProperty("webdriver.chrome.driver", "C:\\chromedriver.exe");

driver = new ChromeDriver();

driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);

}

@Test

public void test1() {

driver.get("https://myt-sit.fhcdn.dev/auth/login");

driver.findElement(By.id("username")).sendKeys("703344343");

driver.findElement(By.id("continue")).click();

}

@AfterMethod

public void tearDown() {

driver.quit();

}

}