// NOT YET FINISHED, TESTS ARE STILL FAILING

import java.util.List;
import java.util.ArrayList;
import org.springframework.util.StringUtils;
import java.util.Collections;

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
            if ((int) carPlate.charAt(i) > 96 && (int) carPlate.charAt(i) < 123) {
                wordList.add(carPlate.charAt(i));
            }
        }

        // Iterate through the list of vocabulary and compare the letters in the plate with each vocabulary
        if (vocabulary.size() == 0) {
            return "";
        }

        for (int i=0; i < vocabulary.size(); i++) {
            vocabulary.get(i) = vocabulary.get(i).toLowerCase();
            matchingCounter = 0;
            seenChar = new ArrayList<Character>();
            for (int j=0; j < wordList.size(); j++) {
                // Count the number of occurences of a character in each vocabulary and in wordList
                int countInVocabulary = StringUtils.countOccurrencesOf(vocabulary[i], wordList[j]);
                int countInwordList = Collections.frequency(wordList, wordList[j]); 
                if (vocabulary.get(i).contains(wordList.get(j))) {
                    if (seenChar.contains(wordList.get(j)) && countInVocabulary == countInwordList) {
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
            matchingVocabs.add(Pair.with(matchingCounter, vocabulary.get(i)));
            }
        }

        // Grab the highest number of matched letters
        int maxCounter = 0;
        for (int counter=0; counter < matchingVocabs.size(); counter++) {
            if (matchingVocabs.getValue(counter).getValue0() > maxCounter)
                maxCounter = matchingVocabs.getValue(counter).getValue0();
        }

        if (maxCounter == 0) {
            return "";
        }

        // Filter the vocabulary, grabing only the ones with the highest max_counter
        for (int pair=0; pair < matchingVocabs.size(); pair++) {
            if (matchingVocabs.getValue(pair).getValue0() == maxCounter)
                finalList.add(matchingVocabs.getValue(pair).getValue1());
        }

        // Return the shortest word matched with the letters in the 'plate' string
        String shortest = finalList.get(0);
        for (String element : finalList) {
            if (element.length() < shortest.length()) {
                shortest = element;
            }
        }
        return shortest;
    }
}