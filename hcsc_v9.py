import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)

player_scores = [0, 0]
current_player = 0
waiting_for_space = True  # Flag to wait for a space bar press
waiting_for_next_calculation = False  # Flag to wait for the space bar to start the next calculation

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)

    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 1, 0, 0, 0] and waiting_for_space:
                player_scores[current_player] += 1
                waiting_for_space = False  # Hand sign recorded, wait for the next space bar press
                waiting_for_next_calculation = True  # Ready for the next calculation
            elif fingerup == [0, 1, 1, 0, 0] and waiting_for_space:
                player_scores[current_player] += 2
                waiting_for_space = False
                waiting_for_next_calculation = True
            elif fingerup == [0, 1, 1, 1, 0] and waiting_for_space:
                player_scores[current_player] += 3
                waiting_for_space = False
                waiting_for_next_calculation = True
            elif fingerup == [0, 1, 1, 1, 1] and waiting_for_space:
                player_scores[current_player] += 4
                waiting_for_space = False
                waiting_for_next_calculation = True
            elif fingerup == [1, 1, 1, 1, 1] and waiting_for_space:
                player_scores[current_player] += 5
                waiting_for_space = False
                waiting_for_next_calculation = True
            elif fingerup == [1, 0, 0, 0, 0] and waiting_for_space:
                player_scores[current_player] += 6
                waiting_for_space = False
                waiting_for_next_calculation = True

    cv2.putText(img, f"Player 1 Score: {player_scores[0]}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(img, f"Player 2 Score: {player_scores[1]}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(img, f"Current Player: {current_player + 1}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    if waiting_for_space:
        cv2.putText(img, "Press 'Space' to Record Hand Sign", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    elif waiting_for_next_calculation:
        cv2.putText(img, "Press 'Space' to Start Next Calculation", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Hand Cricket", img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord(' '):
        if waiting_for_next_calculation:
            waiting_for_space = True  # Wait for the next space bar press
            waiting_for_next_calculation = False  # Reset the flag for the next calculation
    elif key == 13:  # Check for Enter key (key code 13)
        if waiting_for_next_calculation:
            current_player = 1 - current_player  # Toggle player
            waiting_for_space = True  # Wait for the next space bar press
            waiting_for_next_calculation = False

video.release()
cv2.destroyAllWindows()
