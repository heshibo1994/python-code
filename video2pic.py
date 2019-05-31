from collections import deque
from multiprocessing.pool import ThreadPool

import cv2 

VIDEO_SOURCE = 0


def process_frame(frame,c):
    # some intensive computation...
    cv2.imwrite('data//20190514factory//data1//' + str(c) + '.jpg', frame)  # 存储为图像
    return frame


if __name__ == '__main__':
    # Setup.
    cap = cv2.VideoCapture('data//20190514factory//DJI_0032.MOV')
    thread_num = cv2.getNumberOfCPUs()
    pool = ThreadPool(processes=thread_num)
    pending_task = deque()
    c = 0
    while True:

        # Consume the queue.
        while len(pending_task) > 0 and pending_task[0].ready():
            res = pending_task.popleft().get()
            cv2.imshow('threaded video', res)

        # Populate the queue.
        if len(pending_task) < thread_num:
            frame_got, frame = cap.read()
            if frame_got:
                task = pool.apply_async(process_frame, (frame.copy(),c))
                pending_task.append(task)
        c = c+1
        # Show preview.
        if cv2.waitKey(1) == 27 or not frame_got:
            break

cv.destroyAllWindows()