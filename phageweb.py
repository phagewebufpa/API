3
���\�	  �               @   s�   d dl Z d dlZd dlZdd� Zdd� Zddd	�Zd
d� Zdd� Zdd� Ze	ej
�dkr�e� Zeej
�Zeeed ed ed ed �Zxee�dkr�ejd� q�W ee� ne�  dS )�    Nc              C   s   d} t | � d S )NzrPHAGEWEB: 
     run: python3 api.py --file inpu_file.gbk --id 80 --integrity 80 --cds 6 --email 'example@mail.com')�print)�msg� r   �main.py�help_message   s    r   c              C   sJ   d} t j| �}|jdkrB|j}||jd�td� |jd�� }|S dS d S )Nz8http://computationalbiology.ufpa.br/phageweb/analyse.php��   zanalysis/20z	analysis/z
/blast.phpF)�requests�get�status_code�text�find�len)�url�request�page�coder   r   r   �get_code   s    

 r   �80�6c       
      C   s@   d|  d }dt |d�i}|d|||| d�}tj|||d�}	|	S )Nz6http://computationalbiology.ufpa.br/phageweb/analysis/z
/blast.phpZarquivo�rb�1)�emailZemail_select�identity�cds�	integrityZ	protocolo)�files�data)�openr   Zpost)
r   Zfile_gbkr   r   r   r   r   �fileZpayload�rr   r   r   �submit_data   s    r    c             C   s@   dd dddd�}x*| D ]"}||kr| | j |�d  ||< qW |S )Nzdenermaues@gmail.comr   r   )z--emailz--filez--idz--integrityz--cds�   )�index)�argsZxargs�argr   r   r   �get_args%   s    
r%   c             C   s2   d|  }t j|�}|jdkr*|j}|j� S dS d S )NzIhttp://computationalbiology.ufpa.br/phageweb/result_status.php?protocolo=r   F)r   r	   r
   r   �strip)r   r   r   r   r   r   r   �
get_status3   s    

r'   c          
   C   sf   d|  d }dddg}xJ|D ]B}t j|| �}|jdkr|j}t|d��}|j|� W d Q R X qW d S )Nz6http://computationalbiology.ufpa.br/phageweb/analysis/�/zoutput_genbank.gbkzoutput_tabular.tabzoutput_characterization.txtr   �w)r   r	   r
   r   r   �write)r   r   r   r   r   r   �outr   r   r   �	get_files=   s    


r,   r!   z--filez--emailz--idz--cds)Nr   r   r   )r   �sysZtimer   r   r    r%   r'   r,   r   �argvr   r#   r   Zsleepr   r   r   r   �<module>   s    



 
