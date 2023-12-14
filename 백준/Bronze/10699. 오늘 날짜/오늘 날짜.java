import java.util.Date;
import java.text.SimpleDateFormat;
import java.util.TimeZone;

public class Main {
    public static void main(String[] args) {
    Date date = new Date();
    SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
//    String formattedDate = dateFormat.format(today);
    dateFormat.setTimeZone(TimeZone.getTimeZone("Asia/Seoul"));
    System.out.println(dateFormat.format(date));

    }
}