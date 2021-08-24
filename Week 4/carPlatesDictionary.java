import java.util.List;
import org.springframework.util.StringUtils;
import java.utils.Collections;

public class ShortestWordInCarPlate {
    private List<Character> wordList = new ArrayList<Character>();
    private Pair<Integer, String> matchingVocabs;
    private List<Character> seenChar;
    private int matchingCounter = 0;
    private List<String> finalList = new ArrayList<String>();

    public static String findShortestWord(String carPlate, List<String> vocabulary) {
        // Filter the 'plate' string, grabing only letters in lowercase (a-z)
        carPlate = carPlate.toLowerCase();
        for (int i=0; i < carPlate.length(); i++) {
            if ((int) carPlate[i] > 96 && (int) carPlate[i] < 123) {
                wordList.add(carPlate[i]);
            }
        }

        // Iterate through the list of vocabulary and compare the letters in the plate with each vocabulary
        if (vocabulary.size() == 0) {
            return ""
        }

        for (int i=0; i < vocabulary.size(); i++) {
            vocabulary[i] = vocabulary[i].toLowerCase();
            matchingCounter = 0;
            seenChar = = new ArrayList<Character>();
            for (int j=0; j < wordList.length(); j++) {
                // Count the number of occurences of a character in each vocabulary and in wordList
                int countInVocabulary = StringUtils.countOccurrencesOf(vocabulary[i], wordList[j]);
                int countInwordList = Collections.frequency(wordList, wordList[j]); 
                if (vocabulary[i].contains(wordList[j]) {
                    if (seenChar.contains(wordList[j]) && countInVocabulary == countInwordList) {
                        matchingCounter += 2;
                    }
                    else {
                        matchingCounter++;
                    }
                }
                else {
                    matchingCounter = 0;
                    break;
                }
            matchingVocabs.add(Pair.with(matchingCounter, vocabulary[i]))
            }
        }

        // Grab the highest number of matched letters
        

        return "";
    }
}