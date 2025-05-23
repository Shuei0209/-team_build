import java.util.HashMap;
import java.util.Map;
import java.util.Random;

public class sample {
    public static void main(String[] args) {
        Map<String, String[]> wordMap = new HashMap<>();
        wordMap.put("あ", new String[]{"あなたがいるから", "あの日の約束を", "あかるい未来へ"});
        wordMap.put("い", new String[]{"いつもそばにいて", "今、始めよう", "命を大切に"});
        wordMap.put("う", new String[]{"運命感じて", "嬉しい気持ちを", "宇宙のように広く"});
        wordMap.put("え", new String[]{"笑顔の花が咲く", "永遠を願って", "絵のような景色を"});
        wordMap.put("お", new String[]{"想いを届けよう", "大きな声で", "思い出を胸に"});

        String[] chars = {"あ", "い", "う", "え", "お"};
        Random rand = new Random();

        for (String c : chars) {
            String[] options = wordMap.getOrDefault(c, new String[]{c + "から始まる言葉がありません"});
            System.out.println(c + "：" + options[rand.nextInt(options.length)]);
        }
    }
};