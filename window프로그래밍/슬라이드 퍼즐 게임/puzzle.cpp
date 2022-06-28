#include <Windows.h>
#include <TCHAR.H>
#include<stdlib.h>
#include<time.h>
#include"resource.h"


LRESULT CALLBACK WndProc(HWND hwnd, UINT iMsg, WPARAM wParam, LPARAM lParam);
HINSTANCE hInst;
//화면 출력
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpszCmdLine, int nCmdShow)
{
    HWND hwnd;
    MSG msg;
    hInst = hInstance;
    WNDCLASS WndClass;
    WndClass.style = CS_HREDRAW | CS_VREDRAW;
    WndClass.lpfnWndProc = WndProc;
    WndClass.cbClsExtra = 0;
    WndClass.cbWndExtra = 0;
    WndClass.hInstance = hInstance;
    WndClass.hIcon = LoadIcon(NULL, IDI_APPLICATION);
    WndClass.hCursor = LoadCursor(NULL, IDC_ARROW);
    WndClass.hbrBackground = (HBRUSH)GetStockObject(WHITE_BRUSH);
    WndClass.lpszMenuName = NULL;
    WndClass.lpszClassName = _T("Window Class Name");
    WndClass.lpszMenuName = MAKEINTRESOURCE(IDR_MENU1);
    RegisterClass(&WndClass);

    hwnd = CreateWindow(
        _T("Window Class Name"),
        _T("2018E7162 임건우"),
        WS_OVERLAPPEDWINDOW,
        50,
        50,
        1000,
        700,
        NULL,
        NULL,
        hInstance,
        NULL);

    ShowWindow(hwnd, nCmdShow);
    UpdateWindow(hwnd);

    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    return (int)msg.wParam;
}

//이미지에 x,y좌표
struct POS
{
    int ImageX, ImageY;
};

static POS pos[4][4];
//1: 평소 상태 4:4*4 이미지로 변경된 상태
static int state = 1;
//교수님이 올려주신 블로그 참조한 함수들
void OnCreate();
void InitGame(int count);
void swap(int* a, int* b);
void OnLButtonDown(HWND hWnd, LPARAM lParam);
void Move(HWND hWnd, int mx, int my);

LRESULT CALLBACK WndProc(HWND hwnd, UINT iMsg, WPARAM wParam, LPARAM lParam)
{
    HDC hdc, mem1dc;
    PAINTSTRUCT ps;
    
    static HBITMAP hBit, oldBit;
    //게임 시작과, 평소 상태를 나타내는 변수
    static bool  GAMESTART = false, DEVIDE = false;

  
    switch (iMsg)
    {
    //비트맵을 가져옴
    case WM_CREATE:
        hBit = LoadBitmap(hInst, MAKEINTRESOURCE(IDB_BITMAP1));
        break;
    // 메뉴에 대한 정보
    case WM_COMMAND:
        switch (LOWORD(wParam))
        {
            //4*4 를 눌렸을 때 
        case ID_IMAGE_4BY4:
            state = 4;
            break;
            //게임 시작
        case ID_gamestart:
            GAMESTART = true;
            InvalidateRgn(hwnd, NULL, TRUE);
            break;
            // 전체화면 보기
        case ID_IMAGE_SOURCE:
            state = 1;
            GAMESTART = false;
            DEVIDE = false;
            break;
            //게임 종료
        case ID_gameend:
            PostQuitMessage(0);
            break;
        }
        InvalidateRgn(hwnd, NULL, TRUE);
        break;
        //마우스를 눌렸을 떄 
    case WM_LBUTTONDOWN:
        OnLButtonDown(hwnd, lParam);
        break;
    case WM_PAINT:
        hdc = BeginPaint(hwnd, &ps);
        mem1dc = CreateCompatibleDC(hdc);
        oldBit = (HBITMAP)SelectObject(mem1dc, hBit);
        //게임 시작이 아니고 4*4버튼을 눌렸을 때 화면을 출력(섞인 상태)
        if (!GAMESTART)
        {
            switch (state)
            {
            case 4:
                OnCreate();
                break;
            }
        }
        //평소 상태 일때(화면만 출력)
        if (!DEVIDE)
        {
            BitBlt(hdc, 0, 0, 500, 500, mem1dc, 0, 0, SRCCOPY);
            DEVIDE = true;
        }
        //게임 시작 상태
        else
        {
            for (int i = 0; i < state; i++)
            {
                for (int j = 0; j < state; j++)
                {
                    if (GAMESTART && (pos[i][j].ImageX  + pos[i][j].ImageY == 6)) continue;
                    BitBlt(hdc, i * (500 / state), j * (500/ state), 500 / state, 500 / state, mem1dc, (500 / state) * pos[i][j].ImageX, (500 / state) * pos[i][j].ImageY, SRCCOPY);
                }
            }
        }

        SelectObject(mem1dc, hBit);
        DeleteDC(mem1dc);
        EndPaint(hwnd, &ps);
        break;
    case WM_DESTROY:
        DeleteObject(hBit);
        PostQuitMessage(0);
        break;

    }
    return DefWindowProc(hwnd, iMsg, wParam, lParam);
}


void swap(POS* a, POS* b)
{
    int temp = (*b).ImageX;
    (*b).ImageX = (*a).ImageX;
    (*a).ImageX = temp;

    int temp1 = (*b).ImageY;
    (*b).ImageY = (*a).ImageY;
    (*a).ImageY = temp1;
}
void InitGame(int count)
{
    int dx = 3;
    int dy = 3;
    //초기화
    for (int y = 0; y < 4; y++)
    {
        for (int x = 0; x < 4; x++)
        {
            pos[y][x].ImageX = x;
            pos[y][x].ImageY = y;
        }
    }
    //상,하,좌,우 랜덤으로 썩음
    srand(time(NULL));
    for (int i = 0; i < count; i++)
    {
        int dir = rand() % 4;

        switch (dir)
        {
        case 0:
            if (0 <= dx - 1)
            {
                swap(&pos[dy][dx], &pos[dy][dx - 1]);
                dx--;
            }
            break;
        case 1:
            if (dx + 1 < 4)
            {
                swap(&pos[dy][dx], &pos[dy][dx + 1]);
                dx++;
            }
            break;
        case 2:
            if (0 <= dy - 1)
            {
                swap(&pos[dy][dx], &pos[dy - 1][dx]);
                dy--;
            }
            break;
        case 3:
            if (dy + 1 < 4)
            {
                swap(&pos[dy][dx], &pos[dy + 1][dx]);
                dy++;
            }
            break;
        }
    }
   
    
}

void OnCreate()
{
    InitGame(100000);

}
void OnLButtonDown(HWND hWnd, LPARAM lParam)
{
    int mx = LOWORD(lParam) / (500/state );
    int my = HIWORD(lParam) / (500/state );

    Move(hWnd, mx, my);
}

void Move(HWND hWnd, int mx, int my)
{
    
    if (  (0 <= mx - 1) && (pos[mx - 1][my].ImageX == 3 && pos[mx - 1][my].ImageY == 3)) //좌
    {
        swap(&pos[mx][my], &pos[mx - 1][my]);
        
        InvalidateRect(hWnd, NULL, TRUE);
    }
    if ( (mx + 1 < 4) && (pos[mx + 1][my].ImageX == 3 && pos[mx + 1][my].ImageY == 3))//우
    {
        swap(&pos[mx][my], &pos[mx + 1][my]);
        InvalidateRect(hWnd, NULL, TRUE);
    }
    if (  (0 <= my - 1) && (pos[mx][my - 1].ImageX == 3 && pos[mx][my - 1].ImageY == 3)) //하
    {
        swap(&pos[mx][my], &pos[mx][my - 1]);
        InvalidateRect(hWnd, NULL, TRUE);

    }
    if ( (my + 1 < 4) && (pos[mx][my + 1].ImageX == 3 && pos[mx][my + 1].ImageY == 3)) //상
    {
        swap(&pos[mx][my], &pos[mx][my + 1]);
        InvalidateRect(hWnd, NULL, TRUE);
    }

}
