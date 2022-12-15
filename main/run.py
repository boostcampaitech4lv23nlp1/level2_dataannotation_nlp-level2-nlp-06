import subprocess
from dataclasses import dataclass

@dataclass
class Config:
    ## 1. 모델 학습시킬 때 가장 먼저 바꿔야 하는 것
    model_name: str = "klue/roberta-large"
    save_path: str = "/opt/ml/saved_model/klue-roberta-large-typed-mlm.pt" # 최종 모델을 어디에 저장할지
    result_path: str = "/opt/ml/submission/klue-roberta-large-mlm.csv" # 마지막 csv 파일을 어디에 저장할지
    wandb_name: str = "klue-roberta-large-mlm" # wandb 내에서 작업 이름 설정 (중요)
    wandb_group: str = "baseline" # wandb group
    wandb_note: str = "'klue/roberta-large with MLM'" # wandb note
    #'lstm, num_layers=2, bias=True, dropout=0.1, bidirectional=True'
    
    ## 2. 데이터 위치 (csv 파일)

    train_data_path: str = "./dataset/train/train80.csv"
    val_data_path: str = "./dataset/train/valid20.csv"
    test_data_path: str = "./dataset/train/valid20.csv"

    ## 3. 학습 설정
    '''
    train_type = {0: "base-model", 1: "rescent", 2: "curriculum", 3: "kfold"}
    model_type = {0: "base-model", 1: "Masked_QA"}
    input_type = {0: "base-input", 1: "typed_punct_entity", 2: "Masked_QA", 3:"typed_punct_entity_front", 4: "entity_mask", 5: "entity_marker", 6:"typed_entity_marker"} 
    loss_type = {0: CrossEntropy, 1: Weighted_CrossEntropy, 2: FocalLoss}
    '''
    train_type: int = 0
    model_type: int = 1
    input_type: int = 1

    loss_type: int = 0
    pooling: str = "CLS" # 어떤 pooler output을 사용할 것인지 : ["MEAN", "CLS"]
    add_rnn: bool = '' # lstm layer를 BERT head에 추가할 것인가?
    epoch: int = 4
    checkpoint_dir: str = "./results" # Trainer의 학습 checkpoint 저장 경로.
    label_dict_dir: str = None # RECENT : label2num dictionary save path.
    warmup_step: int = 168 # learning rate warmup step.
    eval_step: int = 50 # 모델 평가/저장 step 수.
    entity_from: str = "last" # ["last", "middle"]

    ## 4. 모델 하이퍼파라미터
    num_hidden_layer: int = 0 # BERT 뒤에 linear layer를 몇 개 쌓을지.
    mx_token_size: int = 400 # 문장 최대 길이
    batch_size: int = 16
    lr: float = 3e-5

    ## 5. 한번 바꾸면 바꿀일 없는 설정
    wandb_project: str = "data-construction"
    wandb_entity: str = "ymnseol"
    '''
    input type 에 대한 자세한 설명
    input type = 0  base_input                          :   박수현 [SEP] 시청 [SEP] 박수현은 오늘 시청에 들렀다.
    input type = 1  typed_entity_marker_punct_kr        :   @ + 사람 + 박수현 @ 은 오늘 # ^ 장소 ^ 시청 # 에 들렀다
    input type = 2  Masked_QA                           :   박수현은 오늘 시청에 들렀다 [SEP] 박수현와 시청의 관계는 [MASK]
    input type = 3  typed_entity_marker_punct_en_front  :   @ + PER + 박수현 @[SEP]# ^ LOC ^ 시청 #[SEP] @ + PER + 박수현 @ 은 오늘 # ^ LOC ^ 시청 # 에 들렀다
    input type = 4  entity_mask                         :   [SUBJ-PER] 은 오늘 [OBJ-LOC] 에 들렀다
    input type = 5  entity_marker                       :   [E1] 박수현 [/E1]은 오늘 [E2] 시청 [/E2] 에 들렀다
    input type = 6  typed_entity_marker                 :   [S:PER] 박수현 [/S:PER] 은 오늘 [O:LOC] 시청 [/O:LOC] 에 들렀다.
    '''

def cmd_parser(dic):
    cmd = "python3 main.py "
    for key in dic:
        param = "--{}={} ".format(key, dic[key])
        cmd += param
    return cmd

if __name__ == "__main__":
    config = Config()
    dic = config.__dict__

    cmd = cmd_parser(dic)
    
    subprocess.call(cmd, shell=True)
